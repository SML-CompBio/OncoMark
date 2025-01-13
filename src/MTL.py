import tensorflow as tf
from tensorflow.keras import layers, models, optimizers, losses
import numpy as np

def train_model(x_train, y_train, t_train_one_hot, 
                          x_val, y_val, t_val_one_hot, 
                          input_shape, num_tasks=10, 
                          batch_size=256, epochs=50, 
                          learning_rate=0.0001, 
                          patience=6, lr_patience=3, 
                          lr_factor=0.5, min_lr=1e-6,
                          save=False,
                          model_save_path='hallmark_model.keras'):
    """
    Trains a multitask model with shared layers and task-specific outputs.

    Args:
        x_train, y_train: Training data and labels.
        t_train_one_hot: One-hot encoded task indicators for training data.
        x_val, y_val: Validation data and labels.
        t_val_one_hot: One-hot encoded task indicators for validation data.
        input_shape: Shape of the input data.
        num_tasks: Number of tasks for multitask learning.
        batch_size: Batch size for training.
        epochs: Number of epochs.
        learning_rate: Initial learning rate for the optimizer.
        patience: Patience for early stopping.
        lr_patience: Patience for learning rate reduction.
        lr_factor: Factor to reduce learning rate by.
        min_lr: Minimum learning rate.
        model_save_path: Path to save the best model.

    Returns:
        A trained model and training/validation loss history.
    """
    
    def create_shared_base(input_shape):
        inputs = layers.Input(shape=input_shape)
        x = layers.Dense(64, kernel_initializer='he_uniform', activation='relu')(inputs)
        return inputs, x

    def create_task_output(shared_layer, num_tasks):
        outputs = []
        for _ in range(num_tasks):
            task_specific_layer = layers.Dense(16, kernel_initializer='he_uniform', activation='relu')(shared_layer)
            task_output = layers.Dense(1, activation='sigmoid')(task_specific_layer)
            outputs.append(task_output)
        return outputs

    # Build the model
    inputs, shared_layer = create_shared_base(input_shape)
    task_outputs = create_task_output(shared_layer, num_tasks)
    model = models.Model(inputs=inputs, outputs=task_outputs)

    # Compile the model
    optimizer = optimizers.Adam(learning_rate=learning_rate)
    task_losses = [losses.BinaryCrossentropy() for _ in range(num_tasks)]
    model.compile(optimizer=optimizer, loss=task_losses)

    best_val_loss = float('inf')
    patience_counter = 0
    lr_patience_counter = 0
    train_loss_list = []
    val_loss_list = []

    for epoch in range(epochs):
        print(f"\nEpoch {epoch + 1}/{epochs}")

        # Training
        combines_loss_list = []
        for i in range(0, len(x_train), batch_size):
            x_batch = x_train[i:i+batch_size]
            y_batch = y_train[i:i+batch_size]
            task_batch = t_train_one_hot[i:i+batch_size]

            with tf.GradientTape() as tape:
                predictions = model(x_batch, training=True)
                task_losses_batch = [
                    task_losses[task](y_batch, predictions[task])
                    for task in range(num_tasks)
                ]
                combined_loss = tf.reduce_mean(task_batch * tf.stack(task_losses_batch, axis=0))
                combines_loss_list.append(combined_loss.numpy())
            
            gradients = tape.gradient(combined_loss, model.trainable_weights)
            optimizer.apply_gradients(zip(gradients, model.trainable_weights))

        # Validation
        val_predictions = model(x_val, training=False)
        val_losses = [
            task_losses[task](y_val, val_predictions[task])
            for task in range(num_tasks)
        ]
        total_val_loss = tf.reduce_mean(t_val_one_hot * tf.stack(val_losses, axis=0))
        avg_train_loss = np.array(combines_loss_list).mean()
        print(f"Training Loss: {avg_train_loss}")
        print(f"Validation Loss: {total_val_loss.numpy()}")
        train_loss_list.append(avg_train_loss)
        val_loss_list.append(total_val_loss.numpy())

        # Early stopping check
        if total_val_loss < best_val_loss:
            best_val_loss = total_val_loss
            patience_counter = 0
            lr_patience_counter = 0
            print("Validation loss improved. Resetting patience and learning rate patience.")
            if save:
                model.save(model_save_path)
            model1 = model
        else:
            patience_counter += 1
            lr_patience_counter += 1
            print(f"No improvement in validation loss. Patience counter: {patience_counter}/{patience}")
            print(f"Learning rate patience counter: {lr_patience_counter}/{lr_patience}")
            
            # Reduce learning rate if no improvement
            if lr_patience_counter >= lr_patience:
                current_lr = optimizer.learning_rate.numpy()
                new_lr = max(current_lr * lr_factor, min_lr)
                optimizer.learning_rate.assign(new_lr)
                print(f"Reducing learning rate to {new_lr}")
                lr_patience_counter = 0

            # Stop training if patience exceeded
            if patience_counter >= patience:
                print("Early stopping triggered. Stopping training.")
                break

    print('Training Done!')
    return model1, train_loss_list, val_loss_list

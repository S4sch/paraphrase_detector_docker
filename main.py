import argparse
import os
import torch

from pytorch_lightning import Trainer, seed_everything
from pytorch_lightning.loggers import TensorBoardLogger

from glue_transformer import GLUETransformer
from glue_data_module import GLUEDataModule

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, default='distilbert-base-uncased')
    parser.add_argument('--checkpoint_dir', type=str, default='models')
    parser.add_argument('--lr', type=float, default=2e-5)
    parser.add_argument('--adam_epsilon', type=float, default=1e-8)
    parser.add_argument('--weight_decay', type=float, default=0.0)
    parser.add_argument('--scheduler_gamma', type=float, default=0.95)
    parser.add_argument('--scheduler_step_size', type=int, default=5)
    parser.add_argument('--train_batch_size', type=int, default=32)
    parser.add_argument('--eval_batch_size', type=int, default=32)
    parser.add_argument('--max_epochs', type=int, default=3)
    parser.add_argument('--gpus', type=int, default=1 if torch.cuda.is_available() else 0)

    args = parser.parse_args()

    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    seed_everything(42)
    dm = GLUEDataModule(
        model_name_or_path="distilbert-base-uncased",
        task_name="mrpc",
    )
    dm.setup("fit")
    model = GLUETransformer(
        model_name_or_path="distilbert-base-uncased",
        eval_splits=dm.eval_splits,
        num_labels=dm.num_labels,
        task_name=dm.task_name,
        learning_rate=args.lr,
        adam_epsilon=args.adam_epsilon,
        weight_decay=args.weight_decay,
        scheduler_gamma=args.scheduler_gamma,
        scheduler_step_size=args.scheduler_step_size,
        train_batch_size=args.train_batch_size,
        eval_batch_size=args.eval_batch_size
    )

    logger = TensorBoardLogger("tb_logs", name=args.model_name)

    trainer = Trainer(
        logger=logger,
        max_epochs=args.max_epochs,
        accelerator="auto",
        devices=args.gpus if args.gpus > 0 else None,
        default_root_dir=args.checkpoint_dir
    )
    trainer.fit(model, datamodule=dm)


if __name__ == "__main__":
    main()

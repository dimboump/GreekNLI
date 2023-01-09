from __future__ import annotations

import datetime
import os
from typing import Any

import pandas as pd


def save_predictions(
    y_true: list[int],
    y_pred: list[int],
    *,
    pipe: Any,
    report: dict[str, dict[str, float]],
    export: bool = False,
    path: str = '../results/predictions',
    comment: str | None = None,
) -> None:
    """Save predictions to a CSV file."""
    try:
        clf = pipe.__class__.__name__
    except AttributeError:
        clf = str(pipe)
    clf = clf.lower().rstrip('classifier')

    f1_macro = report['macro avg']['f1-score']

    df = pd.DataFrame({
        'y_true': y_true,
        'y_pred': y_pred,
    })

    if export:
        if not os.path.exists(path):
            os.makedirs(path)
        datetime_suffix = datetime.datetime.now().strftime("_%Y%m%d_%H%M")
        filename = f"{clf}_{round(f1_macro, 3)}_{datetime_suffix}"
        if comment:
            filename += f"_{comment}"
        df.to_csv(os.path.join(path, f"{filename}.csv"),
                  index=False, encoding='utf-8')

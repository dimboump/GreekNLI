from __future__ import annotations

import datetime
import os
from typing import Sequence

import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline


def plot_cm(
    cm: (np.ndarray | list[list[int]]),
    *,
    pipe: Pipeline | VotingClassifier,
    report: dict[str, dict[str, float]],
    labels: Sequence[str] | None = None,
    cmap: str = 'Blues',
    colorbar: bool = True,
    include_scores: bool = True,
    include_timestamp: bool = True,
    export: bool = False,
    path: str = '../results/figures',
    comment: str | None = None,
) -> None:
    """Plot a confusion matrix."""
    if labels is None:
        labels = [str(i) for i in range(cm.shape[0])]  # type: ignore
    cm_disp = ConfusionMatrixDisplay(cm, display_labels=labels)
    cm_disp.plot(cmap=cmap, colorbar=colorbar)

    try:
        title = pipe.__class__.__name__
    except AttributeError:
        title = str(pipe)

    # if isinstance(pipe, VotingClassifier):
    #     title = pipe.named_estimators['clf'].__class__.__name__
    # elif isinstance(pipe, Pipeline):
    #     title = pipe.named_steps['clf'].__class__.__name__

    f1_macro = report['macro avg']['f1-score']
    accuracy = report['accuracy']
    precision = report['macro avg']['precision']
    recall = report['macro avg']['recall']

    if include_scores:
        subtitle = f"F1 macro: {f1_macro:.3f} | accuracy: {accuracy:.3f}"
        subtitle += f"\nprecision: {precision:.3f} | recall: {recall:.3f}"
        plt.xlabel(f"Predicted label\n{subtitle}")

    plt.title(title, fontsize=14)

    if export:
        plt.title(title, fontsize=14)
        clf = title.lower().rstrip('classifier')

        filename = f"{clf}_{round(f1_macro, 3)}"

        if comment is not None:
            filename += f"_{comment}"
        if include_timestamp:
            now = datetime.datetime.now()
            filename += f"_{now.strftime('%Y%m%d_%H%M')}"

        filename = f"{filename}.svg"
        save_path = os.path.join(path, filename).replace("\\", "/")
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Saved confusion matrix: {save_path}")

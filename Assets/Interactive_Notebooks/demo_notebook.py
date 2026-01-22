import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def _(mo):
    mo.md(
        """
    # Interactive Python Demo

    This is a **reactive** Marimo notebook running entirely in your browser via WebAssembly!
    """
    )
    return


@app.cell
def _(mo):
    mo.md("""## Try It: Interactive Slider""")
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100, value=50, label="Select a value:")
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"""**You selected:** {slider.value}""")
    return


@app.cell
def _(mo):
    mo.md("""## Visualization: Sine Wave""")
    return


@app.cell
def _(np, plt, slider):
    # Generate data based on slider
    x = np.linspace(0, slider.value / 10, 100)
    y = np.sin(x)

    # Create plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, 'b-', linewidth=2)
    ax.set_title(f'Sine Wave (0 to {slider.value / 10:.1f})')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## How It Works

    - **Reactive**: When you move the slider, the plot automatically updates!
    - **No Backend**: Everything runs in your browser using WebAssembly
    - **Edit & Run**: You can edit any cell and see changes immediately

    Try changing the slider value above and watch the plot update automatically.
    """
    )
    return


if __name__ == "__main__":
    app.run()

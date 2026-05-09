# Downloading PaperVision

## Bundled with EOCV-Sim (recommended)

PaperVision ships bundled inside EOCV-Sim — no separate download needed. Together they form a complete vision development suite: EOCV-Sim handles pipeline execution in the background while PaperVision gives you a visual, fully previewable node-based editor on top of it.

<div class="promo-card">
  <span class="promo-icon"><i class="fa-solid fa-laptop" aria-hidden="true"></i></span>
  <div class="promo-body">
    <p class="promo-title">Download via EOCV-Sim</p>
    <p class="promo-desc">PaperVision is included in every EOCV-Sim release. Download EOCV-Sim to get both tools in a single package.</p>
  </div>
  <a class="promo-btn" href="/eocv-sim/downloading-eocv-sim.html">Download EOCV-Sim →</a>
</div>

Once launched, switch to the **PaperVision** tab in the top-right corner of the EOCV-Sim window to create and run your projects.

<img src="assets/image (4) (1) (1).png" alt="PaperVision tab in EOCV-Sim" class="screenshot-sm">

## Running from source (development)

You can also run PaperVision directly from source using Gradle. This is useful for testing the latest unreleased changes or contributing to the project.

```bash
git clone https://github.com/deltacv/PaperVision.git
cd PaperVision
./gradlew runEv
```

> [!NOTE]
> Standalone PaperVision does not currently support live pipeline previews. While you can still design and export pipelines, real-time visual feedback is only available when using PaperVision through the EOCV-Sim bundle.

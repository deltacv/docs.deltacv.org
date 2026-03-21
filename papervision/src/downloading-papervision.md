# Downloading PaperVision

## Bundled with EOCV-Sim (recommended)

PaperVision is bundled inside [EOCV-Sim](https://app.gitbook.com/s/-Mj4bZXgCUnwOLKFxDRi/), making an all-in-one vision development suite.

To download EOCV-Sim, [follow the steps in the documentation](https://app.gitbook.com/s/-Mj4bZXgCUnwOLKFxDRi/downloading-eocv-sim).

> [!NOTE]
> Locate to the PaperVision tab on the top right of EOCV-Sim to start making your own projects.

![PaperVision Tab in EOCV-Sim](<assets/image (4) (1) (1).png>)

## Running from Gradle (development and testing)

Use the following commands to run the project with Gradle, this will allow you to test the latest features and changes, building from source.

```bash
git clone https://github.com/deltacv/PaperVision.git
cd PaperVision
./gradlew runEv
```

PaperVision relies on EOCV-Sim to run pipelines with live previews. This means that if you run PaperVision on its own, you won’t be able to see the pipeline’s output in real time. However, you can still use the editor to design your pipelines and export the generated source code for use elsewhere.

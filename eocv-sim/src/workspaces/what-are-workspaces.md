# Workspaces

A workspace is a folder containing `.java` source files and resource files that EOCV-Sim compiles on-the-fly. This means you don't need to run Gradle builds — changes are picked up and applied within seconds.

![A OpenCvPipeline opened in VS Code with IntelliSense](../assets/screenshot\_2021-09-08\_13-29-02.png)

## Selecting a workspace

Workspaces aren't tied to any specific IDE or text editor — you just need to point EOCV-Sim at a folder containing `.java` files. A `eocvsim_workspace.json` file in the folder controls the build process (covered in the next section).

By default, the sim creates and uses a workspace at `~/.eocvsim/default_workspace`, which includes a sample `GrayscalePipeline.java`. To switch to a different folder:

* Go to the "Pipelines" section and click **Workspace → Select workspace**

![](../assets/eocvsim\_usage\_workspace\_select.gif)

* Select a folder in the file explorer that opens

![](../assets/file-chooser-screenshot.png)

* The sim will set the selected folder as the active workspace, generate a `eocvsim_workspace.json` if one doesn't exist, and compile the `.java` files inside.

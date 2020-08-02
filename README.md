# DRF Sandbox

Just playing around with Django REST Framework, authentication, and stuff...



## Managing Conda Environment and Dependencies


### Creating an environment from an existing `environment.yml` file

```bash
cd $WORKSPACE_DIRECTORY/drf_sandbox
conda env create --name environment.yml
conda activate drf_sandbox
```

### Activating/Deactivating the environment

```bash
conda activate drf_sandbox
conda deactivate drf_sandbox
```

### Removing the environment

```bash
conda env remove --name drf_sandbox
```

### Updating the environment

```bash
conda activate drf_sandbox # Make sure that the environment is active.
conda env export --no-builds --from-history
```
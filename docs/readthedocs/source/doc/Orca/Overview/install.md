# Installation

We recommend using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) to prepare the Python environment. Install conda and create an environment for BigDL Orca:
```bash
conda create -n py37 python=3.7  # "py37" is conda environment name, you can use any name you like.
conda activate py37
```

## To use basic Orca features
You can install Orca in your created conda environment for distributed data processing, training and inference with the following command:
```bash
pip install bigdl-orca  # For the official release version
```

or for the nightly build version, use:
```bash
pip install --pre --upgrade bigdl-orca  # For the latest nightly build version
```

## To additionally use RayOnSpark

If you wish to run [RayOnSpark](ray.md) or [sklearn-style Estimator APIs in Orca](distributed-training-inference.md) with "ray" backend, use the extra key `[ray]` during the installation above:

```bash
pip install bigdl-orca[ray]  # For the official release version
```

or for the nightly build version, use:
```bash
pip install --pre --upgrade bigdl-orca[ray]  # For the latest nightly build version
```

Note that with the extra key of [ray], `pip` will automatically install the additional dependencies for RayOnSpark,
including `ray[default]==1.9.2`, `aiohttp==3.8.1`, `async-timeout==4.0.1`, `aioredis==1.3.1`, `hiredis==2.0.0`, `prometheus-client==0.11.0`, `psutil`,  `setproctitle`.

## To additionally use AutoML

If you wish to run AutoML, use the extra key `[automl]` during the installation above:

```bash
pip install bigdl-orca[automl]  # For the official release version
````

or for the nightly build version, use:
```bash
pip install --pre --upgrade bigdl-orca[automl]  # For the latest nightly build version
```

Note that with the extra key of [automl], `pip` will automatically install the additional dependencies for distributed hyper-parameter tuning,
including `ray[tune]==1.9.2`, `scikit-learn`, `tensorboard`, `xgboost` together with the dependencies given by the extra key [ray].

- To use [Pytorch AutoEstimator](distributed-tuning.md#pytorch-autoestimator), you need to install Pytorch with `pip install torch==1.8.1`.

- To use [TensorFlow/Keras AutoEstimator](distributed-tuning.md#tensorflow-keras-autoestimator), you need to install TensorFlow with `pip install tensorflow==1.15.0`.

# Python Auditory Modeling Toolbox

pambox is a Python toolbox to facilitate the development of auditory models,
with a focus on speech intelligibility prediction models.

The project is maintained by Alexandre Chabot-Leclerc.

pambox provides a consistent API for speech intelligibility models, inspired
by [Scikit-learn](http://scikit-learn.org/), to facilitate comparisons across
models.

### Links:

- Official source code repo:
[https://github.com/achabotl/pambox](https://github.com/achabotl/pambox)
- HTM documentations:
- Issue tracker:
[https://github.com/achabotl/pambox/issues](https://github.com/achabotl/pambox
/issues)
- Mailing list: [python-pambox@googlegroups.com]
(mailto:python-pambox@googlegroups.com)
- Mailing list archive: [https://groups.google.com/d/forum/python-pambox]
(https://groups.google.com/d/forum/python-pambox)


## Dependencies

pambox is tested to work under Python 2.7 and Python 3.4 (thanks to `six`).
Only Mac OS X (10.9) has been tested thoroughly).

The main dependencies are [Numpy](http://www.numpy.org/)>=
1.8.0, [Scipy](http://scipy.org/scipylib/)>=0.14.0,
[Pandas](http://pandas.pydata.org)>=0.14.1,
[six](https://bitbucket.org/gutworth/six) >=1.7.2 (to have a single codebase
for Python 2 and Python 3).
Lower versions of these packages are likely to work as well but have not been
thoroughly tested.

For running tests, you will need [pytest](http://pytest.org/).

## Install

You can simply do:

	pip install pambox

## Contributing

You can check out the latest source and install it for development with:

	git clone https://github.com/achabotl/pambox.git
	cd pambox
	python setup.py develop

To run tests, from the root pambox folder, type:

	py.test

## License

pambox is licensed under the New BSD License (3-clause BSD license).

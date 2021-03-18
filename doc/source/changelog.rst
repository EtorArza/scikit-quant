.. _changelog:

Changelog
=========


2021-03-17: 0.8.1
-----------------

* Make SQNomad optional (use option [NOMAD]) as it is rather slow to install


2020-11-30: 0.8.0
-----------------

* Added SQNomand
* Require rpy2 to be installed separately as ORBIT use is uncommon


2020-05-22: 0.7.0
-----------------

* Added Qiskit interoperability interface
* Added SciPy interoperability interface
* Fixed a couple of logic flow bugs in SnobFit
* Fix number of requests if nreq=1 (SnobFit; Jan Rittig)
* Fix indexing error and double delete in NaN handling (SnobFit; Jan Rittig)


2020-04-28: 0.6.0
-----------------

* Remove use of numpy.matrix in SQImFil
* Bug fixes in SQCommon and SQSnobFit
* Start of documentation

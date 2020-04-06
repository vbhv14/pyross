## PyRoss: Infectious disease models in Python.



![Imagel](/banner.png)

## About:

[PyRoss](https://gitlab.com/rajeshrinet/pyross) is a numerical library for mathematical modelling of infectious disease in Python. The library supports structured compartment models formulated as systems of differential equations. Currently, these are the **SIR**, **SEIR**, **SEAIR**, and **SEAIRQ** models. 

The library was developed to model the outbreak of the novel coronavirus COVID-19 and to assess the age-structured impact of social distancing measures in India. 

The library is named after [Sir Ronald Ross](https://en.wikipedia.org/wiki/Ronald_Ross), doctor, mathematician and poet. In 1898 he made "the great discovery" in his laboratory in Calcutta "that malaria is conveyed by the bite of a mosquito".  He won the Nobel Prize in 1902 and laid the foundations of the mathematical modelling of infectious diseases. 


## For forked implepention Related queries: 

Kindly, raise an issue on GitHub.


## Installation for forked implementation:

Clone (or download) the repository. 

create a new conda env. or clone the ArcGIS Pro default env. using the the environment file.

then in the python command prompt, go to the cloned directory and type:

```Python
python setup.py install
```


## Data sources:

Age and social contact data that is needed to construct structured compartment models can be found at the following links:

**Age structure:** [Population Pyramid](https://www.populationpyramid.net/) website. 

**Contact structure:** *Projecting social contact matrices in 152 countries using contact surveys and demographic data*, Kiesha Prem, Alex R. Cook, Mark Jit, PLOS Computational Biology, (2017) [DOI]( https://doi.org/10.1371/journal.pcbi.1005697), [Supporting Information Text](https://doi.org/10.1371/journal.pcbi.1005697.s001)  and [Supporting Information Data](https://doi.org/10.1371/journal.pcbi.1005697.s001).

The list of COVID-19 cases is obtained from the [Worldometer website](https://www.worldometers.info/coronavirus).


## Author's Contact Info:

The authors are part of [The Rapid Assistance in Modelling the Pandemic (RAMP) ](https://www.maths.cam.ac.uk/features/call-action-covid-19) taskforce. We can be contacted at: rs2004@cam.ac.uk (Rajesh Singh) and ra413@cam.ac.uk (R. Adhikari). 



## Link to original author's paper:

* [Age-structured impact of social distancing on the COVID-19 epidemic in India](https://github.com/rajeshrinet/pyross/blob/master/draft/covid19.pdf), Rajesh Singh and R. Adhikari, [arXiv:2003.12055](https://arxiv.org/abs/2003.12055).


* See the author's examples at [examples folder](https://github.com/rajeshrinet/pyross/tree/master/examples) .


## License:
This code is released under the [MIT license](http://opensource.org/licenses/MIT).

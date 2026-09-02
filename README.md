<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# StrenDCAT-Biocatalysis

Aligning StrendaBiocatalysis guidelines to the DCAT-AP Plus schema.

## Documentation Website

[https://mvoelken-hub.github.io/StrenDCAT-Biocatalysis](https://mvoelken-hub.github.io/StrenDCAT-Biocatalysis)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [strendcat_biocatalysis](src/strendcat_biocatalysis)
    * [schema/](src/strendcat_biocatalysis/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/strendcat_biocatalysis/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Run EnzymeML-Converter

uv run python -m strendcat_biocatalysis.enzymeml_converter <input_file> -o <output_file> -v

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).

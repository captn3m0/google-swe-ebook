# swe-ebook

Generates a EPUB/MOBI/PDF for the Google SWE Book. Original sources are downloaded from https://abseil.io/resources/swe-book.

> The Software Engineering at Google book (“SWE Book”) is not about programming, per se, but about the engineering practices utilized at Google to make their codebase sustainable and healthy. (These practices are paramount for common infrastructural code such as Abseil.)

If you like the book, please [purchase a copy](https://www.oreilly.com/library/view/software-engineering-at/9781492082781/).

An official (older) PDF copy of the book is also available at <https://raw.githubusercontent.com/abseil/abseil.github.io/cd13b21daa6ec74155548241241693198c1b1264/resources/swe_at_google.2.pdf>.

If you liked this project, you might also like [Google SRE Ebook Generator](https://github.com/captn3m0/google-sre-ebook).

## Usage

You must have `pandoc` and `python3` installed.

```sh
git clone https://github.com/captn3m0/google-swe-ebook.git
cd google-swe-ebook
python3 -m venv venv --prompt="dev-env"
source venv/bin/activate
pip install panflute
# To generate EPUB
pandoc --defaults=epub.yaml
# To generate PDF
pandoc --defaults=pdf.yaml
```

## Docker

A simple docker image is available.

```sh
# replace $(pwd) with the path to your output directory

# Generate the EPUB file
docker run --volume $(pwd):/src/output captn3m0/google-swe-ebook --defaults=epub.yaml

# Generate the PDF file
docker run --volume $(pwd):/src/output captn3m0/google-swe-ebook --defaults=pdf.yaml

# You can generate other formats, but these are unsupported
docker run --volume $(pwd):/src/output captn3m0/google-swe-ebook --defaults=epub.yaml --to html5 -s -o /src/output/output.html
```

# How

This uses a pandoc configuration, along with a small Python filter
(writtein in panflute) to generate decently good PDF/EPUB files.

## Known Issues

PDF links are slightly wonky.

## License

Licensed under the [MIT License](https://nemo.mit-license.org/). See LICENSE file for details.
# Data-driven documentation

The purpose of choosing a Jupyter notebook, instead of the conventional document processing software like Word or even modern Canvas boards, is manyfold - taken from [JupDoc](https://pypi.org/project/jupdoc/).

It is possible to write a very light wrapper like [JupDoc](https://pypi.org/project/jupdoc/) written in Python that simplifies publishing Jupyter notebooks into multiple docx files or other formats while applying view-based filters based on cell tags. One can use modern publishing software like [Quarto](https://quarto.org/) to achieve this.

With a notebook converter like JupDoc based on Quarto, designed to publish data-driven documentation, one needs to
- Render the notebook into any format, filtered by the tag, for that stakeholder
- From a single notebook, create as many views/docs as needed based on cell tags
- Convert ipynb notebooks to docx, pdf, HTML tex, MD
- Upload the generated files to Google Drive (need service account) or other cloud storage formats
- Maintain a single source of truth
- Automate document publishing
- No broken, stale, docs with different versions of the data floating around

In addition, a typical requirement for documentation is - different stakeholders (like Business Executives, Product Managers, and ML Scientists, among others) need different information to act. Often, the format, content, and emphasis will be different. Further, they want documents that are:
- Accurate (and up to date)
- Available
- Accessible
- Reproducible
- Audutiable
- Versioned
- Serves their needs (w.r.t content, format, style, accessibility, shareability, etc.)

But, an ML Developer can only deliver on some fronts. Conventionally,
- Development and Documentation are not part of the same process. The toolset and mindset are different, even separated in time & space.
- Even a simple edit or change request requires a copy-and-paste from somewhere. If data or ask or both change, one must redo the documentation repeatedly. This is neither repeatable nor reproducible and also not sustainable.

As a result, a rigorous process oversight is needed for compliance. For example, a reporting manager may periodically check if the documentation is maintained and up to date as a part of the review processing. But this is not sustainable. We know it all too well.

## Solution
- Surprisingly simple. Just tag a notebook cell - who is it for?
- And take benefit of modern document publishing tools and workflows like Quarto, GitHub, GitHub actions

## Core tenets

- One content - many views
- Data + Code  + Content > should drive the documentation (format, style, purpose)
- Each stakeholder’s documentation need is just a view or a content rendering problem
- Publishing documentation =  Publishing code
- Use the same tools and mental models both for code and documents
- Single source of truth for any derived document
- Fix in only one place and only once.
- Physical and mental distance between Documentation and Code should be (close to) ZERO
- Set up once and automate subsequently
- Automate the publishing process
- No human oversight should be necessary for process compliance
- Commit code + documentation content > rendering must be automated


## Features

- Define views using cell tags.
- Convert Jupyter Notebooks to docx, PDF, HTML, and more.
- Generate separate documents for each view.

## Benefits
Data-driven documents enable
- reproducibility, auditing, versioning, accuracy,

- When code blocks read data (e.g.,  ground truth vs. predictions), documents can be up to date also.

## A new mindset
- Writing documents is the same as writing code in the same place, space, and time.
- The stakeholder needs can be arranged in a hierarchy while authoring content via content inheritance. Executive Summary < Model Card < Solution Card < Full Report!
- To drive reports and visualization (of evaluation metrics), read data, and run code - so that whenever models/data are updated, metrics are also updated automatically!

*Note:*
1. _The conversion of .ipynb is based on Quarto, and custom rending can be done by adding yaml config specific to notebooks as raw cells._
2. _All cells in the notebook should have tags (including markdown cells), and the tags should be a part of the config used to export._
3. _Quarto cheat sheet can be refered from [here](https://images.datacamp.com/image/upload/v1676540721/Marketing/Blog/Quarto_Cheat_Sheet.pdf). Details can be provided in the raw cell for customizations on reports._
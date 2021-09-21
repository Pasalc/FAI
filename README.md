Фундаментальные концепции искусственного интеллекта
# Датасет:
https://www.kaggle.com/Cornell-University/arxiv - Метаданные 1.7 миллионов статей с сайта arXiv в формате json.

# Метаданные:

    id: ArXiv ID (can be used to access the paper, see below)
    submitter: Who submitted the paper
    authors: Authors of the paper
    title: Title of the paper
    comments: Additional info, such as number of pages and figures
    journal-ref: Information about the journal the paper was published in
    doi: [https://www.doi.org](Digital Object Identifier)
    abstract: The abstract of the paper
    categories: Categories / tags in the ArXiv system
    versions: A version history

# Доступ к статьям через ссылки:

    https://arxiv.org/abs/{id}: Page for this paper including its abstract and further links
    https://arxiv.org/pdf/{id}: Direct link to download the PDF

# Много статей за один раз:
  List files:
  gsutil cp gs://arxiv-dataset/arxiv/

  Download pdfs from March 2020:
  gsutil cp gs://arxiv-dataset/arxiv/arxiv/pdf/2003/ ./a_local_directory/

  Download all the source files
  gsutil cp -r gs://arxiv-dataset/arxiv/  ./a_local_directory/

import reflex as rx

from reflex.components.component import NoSSRComponent

# class File(rx.Component):
#     """A custom loading icon component."""
#     library = './resume.pdf'
#     tag = ""
#     url: rx.Var[str] = "/resume.pdf"


class PDFDoc(rx.Component):
    """A custom loading icon component."""
    library = "@react-pdf/renderer"
    tag = "Document"
    file: rx.Var[str] = "/resume.pdf"

class PDFPage(rx.Component):
    """A custom loading icon component."""
    library = "@react-pdf/renderer"
    tag = "Page"
    pageNumber: rx.Var[int] = 1



class PDFWorker(rx.Component):
    """PDF Worker Component."""

    library = "@react-pdf-viewer/core@3.12.0"
    lib_dependencies: list[str] = ["pdfjs-dist@3.4.120"]

    tag = "Worker"

    workerUrl: rx.Var[str] = "https://unpkg.com/pdfjs-dist@3.4.120/build/pdf.worker.min.js"




class PDFViewer(PDFWorker):
    """PDF Viewer Component."""

    library = "@react-pdf-viewer/core@3.12.0"
    plugins: list[str] = ["@react-pdf-viewer/default-layout@3.12.0"]

    tag = "Viewer"

    fileUrl: rx.Var[str] = "/resume.pdf"
    
    def _get_custom_code(self) -> str:
        return"""import '@react-pdf-viewer/core/lib/styles/index.css';
                import '@react-pdf-viewer/default-layout/lib/styles/index.css';"""

worker = PDFWorker.create
viewer = PDFViewer.create

doc = PDFDoc.create
page = PDFPage.create




import base64
from math import ceil

class NewSVG:

    def __init__(self, size=(700,700)):
        self.document = []
        self.width, self.height = size
        self.create_document()

    def create_document(self):
        header = [
            '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
            "<!-- Created with Inkscape (http://www.inkscape.org/) -->",
            "",
            "<svg",
            '   width="{}px"'.format(self.width),
            '   height="{}px"'.format(self.height),
            '   viewBox="0 0 {} {}"'.format(self.width,self.height),
            '   version="1.1"',
            '   id="svg1"',
            '   inkscape:version="1.1.1 (3bf5ae0d25, 2021-09-20)"',
            '   sodipodi:docname="drawing.svg"',
            '   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"',
            '   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"',
            '   xmlns:xlink="http://www.w3.org/1999/xlink"',
            '   xmlns="http://www.w3.org/2000/svg"',
            '   xmlns:svg="http://www.w3.org/2000/svg">',
            '  <sodipodi:namedview',
            '     id="namedview1"',
            '     pagecolor="#505050"',
            '     bordercolor="#eeeeee"',
            '     borderopacity="1"',
            '     inkscape:pageshadow="0"',
            '     inkscape:pageopacity="0"',
            '     inkscape:pagecheckerboard="0"',
            '     inkscape:document-units="px"',
            '     showgrid="false"',
            '     units="px"',
            '     inkscape:zoom="1.0"',
            '     inkscape:cx="0"',
            '     inkscape:cy="0"',
            '     inkscape:window-width="1920"',
            '     inkscape:window-height="1057"',
            '     inkscape:window-x="-8"',
            '     inkscape:window-y="-8"',
            '     inkscape:window-maximized="1"',
            '     inkscape:current-layer="layer1" />',
            '  <defs id="defs2" />'
        ]
        self.document.append("\n".join(header))

    def add_image(self, index, layer):
        
        def encode(image_path):
            '''
            Encode an image into base64.
            :param image_path: str -> Path for the image
            :return prettyfy_b64: str -> Encoded base64 image
            '''
            with open(image_path, "rb") as img_file:
                b64 = base64.b64encode(img_file.read()).decode('utf-8')
                max_column = ceil(len(b64)/76) + 1
                rows = [i*76 for i in range(0,max_column)] 
                rows[-1] = len(b64)
                prettify_b64 = []
                for j in range(len(rows)-1):
                    a,b = rows[j],rows[j+1]
                    prettify_b64.append(b64[a:b])
                return "\n".join(prettify_b64)

        def encode_image(detail, size):
            '''
            Creating group tag for XML document.
            :param data: dict -> Trait information based on the image file from source_images
            :param size: tupple -> SVG Document size
            :return layer: XML group tag for the image
            '''
            layer = [
                '  <g',
                '    inkscape:groupmode="layer"',
                '    id="layer{}"'.format(detail['index']),
                '    style="display:none"',
                '    inkscape:label="{}">'.format(detail['attribute_name']),
                '    <image',
                '        width="{}"'.format(size[0]),
                '        height="{}"'.format(size[1]),
                '        preserveAspectRatio="none"',
                '        xlink:href="data:image/png;base64,{}"'.format(encode(detail['image_path'])),
                '        id="image{}"'.format(detail['index']),
                '        x="0"',
                '        y="0" />',
                '    </g>'
            ]
            return "\n".join(layer)

        detail = {
            "index": index,
            "attribute_name": layer['attribute_name'],
            "image_path": layer['path']
        }

        image = encode_image(detail, size=(self.width,self.height))

        self.document.append(image.rstrip())

    def save(self, file_path="source\\source.svg"):

        self.document.append("</svg>")
        self.document = "\n".join(self.document)
        
        with open(file_path,"w") as f:
            f.write(self.document)
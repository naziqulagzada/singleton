import json
import xml.etree.ElementTree as ET


class XmlDataSource:
    def get_data(self):
        return """<person>
                    <name>Ali</name>
                    <age>25</age>
                  </person>"""

class JsonAnalyzer:
    def analyze(self, data: dict):
        print("Analyze data...")
        print(data)

class XmltoJsonAdaptor:
    def __init__(self, xml_source: XmlDataSource):
        self.xml_source = xml_source

    def get_json_data(self):
        xml_data = self.xml_source.get_data()
        root = ET.fromstring(xml_data)
        data_dict = {child.tag: child.text for child in root}
        return json.dumps(data_dict)

if __name__ == "__main__":
    xml_source = XmlDataSource()
    adapter = XmltoJsonAdaptor(xml_source)
    analyzer = JsonAnalyzer()

    json_data = adapter.get_json_data()
    analyzer.analyze(json.loads(json_data))


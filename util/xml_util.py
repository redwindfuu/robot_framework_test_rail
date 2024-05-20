import xml.etree.ElementTree as ET


class XmlUtil:
    def __init__(self, file_path):
        """
        Khởi tạo đối tượng XmlUtil với đường dẫn đến file XML.

        Args:
            file_path (str): Đường dẫn đến file XML.
        """
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()

    def get_element_by_tag(self, tag_name):
        """
        Lấy phần tử đầu tiên có tên tag cụ thể.

        Args:
            tag_name (str): Tên tag cần tìm.

        Returns:
            Element: Phần tử XML đầu tiên tìm thấy, hoặc None nếu không tìm thấy.
        """
        return self.root.find(tag_name)

    def get_elements_by_tag(self, tag_name):
        """
        Lấy tất cả các phần tử có tên tag cụ thể.

        Args:
            tag_name (str): Tên tag cần tìm.

        Returns:
            list: Danh sách các phần tử XML tìm thấy.
        """
        return self.root.findall(tag_name)

    def get_element_by_path(self, path):
        """
        Lấy phần tử theo đường dẫn XPath.

        Args:
            path (str): Đường dẫn XPath đến phần tử.

        Returns:
            Element: Phần tử XML tìm thấy, hoặc None nếu không tìm thấy.
        """
        return self.root.find(path)

    def get_child_elements(self, parent_element, child_tag=None):
        """
        Lấy các phần tử con của một phần tử cha.

        Args:
            parent_element (Element): Phần tử cha.
            child_tag (str, optional): Tên tag của phần tử con cần tìm (mặc định là None, trả về tất cả các phần tử con).

        Returns:
            list: Danh sách các phần tử con tìm thấy.
        """
        if child_tag is None:
            return list(parent_element)  # Trả về tất cả các phần tử con
        else:
            return parent_element.findall(child_tag)

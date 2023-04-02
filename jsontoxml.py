import json
import xmltodict


def convert():
    # filecategory = "Data_Reports"
    category = "Data_Banners_2022_Onward"
    with open(f"PagesExport/{category}.json", "r") as file:
        python_dict = json.load(file)

        pages_dict = {
            category: {
                "pages": []
            }
        }

        page_count = 0
        file_number = 1

        for page in python_dict['pages']:

            # page['data']['writer'] = page['data']['author']
            # del page['data']['author']
            # del page['data']['teaser_image']
            # del page['data']['images']

            pages_dict[category]['pages'].append(page)

            if page['settings']['id'] == 13664 or page_count == 24:
                xml_file = open(f"{category}_Batch_{file_number}.xml", "wb")
                xmltodict.unparse(pages_dict, output=xml_file)
                xml_file.close()

                print(page_count, page['settings']['id'])
                pages_dict[category]['pages'] = []
                file_number += 1
                page_count = 0
            else:
                page_count += 1


if __name__ == '__main__':
    convert()

"""Layout, blocks layout"""

insitu_report_layout_items = [
    "e1deefa8-4baf-4f36-a95c-83522954e6c6",
    "dea6de57-6ec7-40fd-9e60-4a81fa984175",
    "a8c5df1c-fa06-4627-a2c3-51b51db4096f",
    "f8d311ae-0ac8-42fc-b041-ebdd671aeb4a",
    "c3c8316e-1e6c-4b78-82d1-d76cc2f87f0b",
    "53c154f6-2f06-490b-b652-6c9626795fa8",
]


insitu_report_layout_blocks = {
    "53c154f6-2f06-490b-b652-6c9626795fa8": {"@type": "slate"},
    "a8c5df1c-fa06-4627-a2c3-51b51db4096f": {
        "@layout": "e6376241-007c-4096-b9a8-2b869487ceb8",
        "@type": "description",
        "block": "b705596b-b737-4dd5-bfce-7c9ee1f8ee55",
        "value": [{"children": [{"text": ""}], "type": "p"}],
    },
    "c3c8316e-1e6c-4b78-82d1-d76cc2f87f0b": {
        "@type": "metadataSection",
        "fields": [
            {
                "@id": "0073df56-49dd-448b-b969-49d778c6a455",
                "field": {
                    "id": "topics", "title": "Topics", "widget": "array"},
                "showLabel": "true",
            },
            {
                "@id": "b5277fa4-03b3-4268-ae8b-7ed7d4919039",
                "field": {
                    "id": "geo_coverage",
                    "title": "Geographical coverage",
                    "widget": "geolocation",
                },
                "showLabel": "true",
            },
            {
                "@id": "51026bf2-3a1b-43bb-a639-159ae6a275ed",
                "field": {
                    "id": "temporal_coverage",
                    "title": "Temporal coverage",
                    "widget": "temporal",
                },
                "showLabel": "true",
            },
            {
                "@id": "b9555f2d-1b62-467b-b22c-24fda6c0df5f",
                "field": {
                    "id": "publisher",
                    "title": "Publisher", "widget": "array"},
                "showLabel": "true",
            },
            {
                "@id": "a80913b4-70ce-4a63-97fc-5447bee6a140",
                "field": {
                    "id": "data_provenance",
                    "title": "Add sources for the data used",
                    "widget": "data_provenance",
                },
                "showLabel": "true",
            },
            {
                "@id": "7c1ce1c9-bf85-434e-a60b-9314974d7ec2",
                "field": {
                    "id": "other_organisations",
                    "title": "Other organisations involved",
                    "widget": "array",
                },
                "showLabel": "true",
            },
            {
                "@id": "8fc36080-4025-4ddb-af3d-60bde94214e2",
                "field": {
                    "id": "rights", "title": "Rights", "widget": "textarea"},
                "showLabel": "true",
            },
            {
                "@id": "20cc640c-52c7-40f0-a2f1-253af69ab56c",
                "field": {
                    "id": "copernicus_services",
                    "title": "Copernicus Services",
                    "widget": "array",
                },
                "showLabel": "true",
            },
        ],
        "variation": "default",
    },
    "dea6de57-6ec7-40fd-9e60-4a81fa984175": {
        "@layout": "2a1c5c01-ef66-4c9a-a4a5-33d0ad403636",
        "@type": "metadata",
        "block": "d9cc432d-bce7-47c6-b45b-0d0107216be8",
        "data": {"id": "report_category", "widget": "array"},
    },
    "e1deefa8-4baf-4f36-a95c-83522954e6c6": {
        "@layout": "ffded585-e851-4216-8b41-5c06e7935bb2",
        "@type": "title",
        "block": "bffb8e02-480f-440f-bc67-688d866dd17b",
        "copyrightIcon": "ri-copyright-line",
        "hideContentType": "true",
        "hideCreationDate": "true",
        "hideModificationDate": "true",
        "styles": {},
    },
    "f8d311ae-0ac8-42fc-b041-ebdd671aeb4a": {
        "@layout": "8634da7d-626c-4e95-99e5-4946c2e0db54",
        "@type": "metadata",
        "block": "3c0c8842-0a89-4966-9189-9fc32e0867ad",
        "data": {"id": "file", "widget": "file"},
    },
}

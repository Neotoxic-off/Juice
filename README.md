# Juice
🧃 Website scrapper api

## Options
- Method: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`
- Host: `https://example.com`
- Params: 
```JSON
[
    ["param1", "paramvalue1"]
]
```
- Tag: `img`, `a`, `p`, `...`
- Element: `href`, `src`, `class`, `...`
- Attrs:
```JSON
{
    "class": "avatar",
    "id": "main"
}
```
- Headers:
```JSON
{
    "User-Agent": "Example",
    "Token": "issou"
}
```
- Data:
```JSON
{
    "EXAMPLE": "DATA"
}
```
- Range: `[0, 3]`
- Ptag: `page`, `p`

## Request
- Method: `POST`
- Route: `/scrap`
- Json:
```JSON
{
    "method": "GET",
    "host": "https://github.com/Neotoxic-off",
    "params": [
        ["tab", "repositories"]
    ],
    "tag": "img",
    "element": "src",
    "attrs": {
        "class": "avatar avatar-user width-full border color-bg-default"
    },
    "headers": {},
    "data": {},
    "range": [0, 3],
    "ptag": "page"
}
```

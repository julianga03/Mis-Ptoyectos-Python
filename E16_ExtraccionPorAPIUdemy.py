import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://www.udemy.com/courses/search/?src=ukw&q=ventas",
    "Accept":"application/json, text/plain, */*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"es-ES",
    "Sec-Ch-Ua":"Not.A/Brand;v=8",
    "X-Requested-With":"XMLHttpRequest",
    "X-Udemy-Cache-Campaign-Code":"KEEPLEARNING",
    "X-Udemy-Cache-Marketplace-Country":"CO",
    "X-Udemy-Cache-Release":"1c6cccab05c3153b4a2b",
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin"
}

urlApi = 'https://www.udemy.com/api-2.0/search-courses/?src=ukw&q=ventas&skip_price=true'

response = requests.get(urlApi, headers = headers)

print(response)

#Ver video 61 por que no me aceoto la solicitud con ningun encabezado
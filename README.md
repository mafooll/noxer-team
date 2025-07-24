# noxer-team

## installing

clone git

```bash
git clone https://github.com/mafooll/noxer-team.git
```

rename env.example -> .env && run from /noxer-team:

```bash
make initial
```

or

```bash
git clone https://github.com/mafooll/noxer-team.git &&
cd noxer-team &&
cp .env.example ./.env &&
make initial
```

filters

```curl
curl -X GET "http://localhost:5555/info?name=футболка" -H "Accept: application/json"
```

```json
{
  "total_products": 3,
  "categories": ["Техника", "Одежда", "Кроссовки", "Сладости", "Наушники"],
  "products": [
    {
      "id": 2,
      "name": "Футболка оверсайз женская",
      "price": 3.0,
      "image_url": "https://static-sda.ru/brandbot/tovars/img2.jpg",
      "on_main": true,
      "category": "Одежда"
    },
    {
      "id": 7,
      "name": "Футболка мужская",
      "price": 900.0,
      "image_url": "https://static-sda.ru/brandbot/tovars/t1.jpg",
      "on_main": false,
      "category": "Одежда"
    },
    {
      "id": 8,
      "name": "Футболка оверсайз мужская",
      "price": 1100.0,
      "image_url": "https://static-sda.ru/brandbot/tovars/t2.jpg",
      "on_main": false,
      "category": "Одежда"
    }
  ]
}
```

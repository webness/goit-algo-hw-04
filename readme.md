
### Результати завдання 1

Емпіричні результати демонструють, що:

- **Сортування вставкою** погано працює на великих масивах через складність O(n2).
- **Сортування злиттям** працює набагато краще з великими масивами, що відповідає його складності O(n log ⁡n).
- **Timsort** є найефективнішим загалом, особливо для великих наборів даних, оскільки він використовує як сортування злиттям, так і сортування вставкою для оптимізації продуктивності.

### Висновки

- Комбінація сортування злиттям і сортування вставкою Timsort робить його набагато ефективнішим, особливо для частково відсортованих даних або реальних вхідних даних.
- Вбудовані функції сортування Python (`sorted` і `sort`)  оптимізовані, що робить непотрібним реалізацію спеціальних алгоритмів сортування в більшості випадків.
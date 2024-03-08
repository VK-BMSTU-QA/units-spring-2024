import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

describe('applyCategories function', () => {
    const products: Product[] = [
        {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника', 
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
        {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
        },
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ];

    const categories: Category[] = ['Одежда', 'Для дома'];

    it('should filter products based on selected categories', () => {
        const result = applyCategories(products, categories);
        expect(result).toHaveLength(2);
    });

    it('should return all products if no categories are selected', () => {
        const result = applyCategories(products, []);
        expect(result).toEqual(products);
    });

    it('should handle empty product array', () => {
        const result = applyCategories([], categories);
        expect(result).toEqual([]);
    });
});

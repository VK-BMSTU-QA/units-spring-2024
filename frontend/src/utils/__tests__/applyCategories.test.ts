import { applyCategories } from '../applyCategories';
import { Category, Product } from '../../types';

describe('test apply categories function', () => {
    const testProducts: Product[] = [
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

    const electronic = [testProducts[0], testProducts[3]];
    const clothes = [testProducts[1]];
    const home = [testProducts[2]];

    it('should return list of all products', () => {
        expect(applyCategories(testProducts, [])).toStrictEqual(testProducts);
        expect(applyCategories(testProducts, ['Электроника', 'Для дома', 'Одежда'])).toStrictEqual(testProducts);
    });

    it('should return list of electronic products', () => {
        expect(applyCategories(testProducts, ['Электроника'])).toStrictEqual(electronic);
    });

    it('should return list of clothes', () => {
        expect(applyCategories(testProducts, ['Одежда'])).toStrictEqual(clothes);
    });

    it('should return list of home products', () => {
        expect(applyCategories(testProducts, ['Для дома'])).toStrictEqual(home);
    });

    it('should return list of home products and clothes', () => {
        expect(applyCategories(testProducts, ['Одежда', 'Для дома'])).toStrictEqual([...clothes, ...home]);
    });
});

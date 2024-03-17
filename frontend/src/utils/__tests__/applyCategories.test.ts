import { applyCategories } from "../applyCategories";
import { Product } from '../../types';

describe('test apply categories function', () => {
    const electronicProducts : Product[] = [
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
        {
            id: 5,
            name: 'Телевизор',
            description: '',
            price: 735393,
            category: 'Электроника',
        },
    ]

    const differentProducts : Product[] = [
        {
            id: 1,
            name: 'Кресло',
            description: 'Мягкое',
            price: 1000,
            category: 'Для дома',
        },
        {
            id: 2,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
        {
            id: 3,
            name: 'Шуба',
            description: 'Сделана из эко меха',
            price: 30000,
            category: 'Одежда',
        },
    ]
    
    it('should return products with category Электроника', () => {
        expect(applyCategories(electronicProducts, ['Электроника'])).toStrictEqual(electronicProducts);
    });

    it('should return products with category Электроника and Для дома', () => {
        expect(applyCategories(electronicProducts, ['Электроника', 'Для дома'])).toStrictEqual(electronicProducts);
    });

    it('should return products with category Для дома (empty array)', () => {
        expect(applyCategories(electronicProducts, ['Для дома'])).toStrictEqual([]);
    });

    it('should return products with category Для дома/Одежда/Для дома', () => {
        expect(applyCategories(differentProducts, ['Для дома'])).toStrictEqual([differentProducts[0]]);
        expect(applyCategories(differentProducts, ['Электроника'])).toStrictEqual([differentProducts[1]]);
        expect(applyCategories(differentProducts, ['Одежда'])).toStrictEqual([differentProducts[2]]);
    });

    it('should return products with category Электроника and Одежда', () => {
        expect(applyCategories(differentProducts, ['Электроника', 'Одежда'])).toStrictEqual([differentProducts[1], differentProducts[2]]);
    });

    it('should return products with category Электроника, Одежда and Для дома', () => {
        expect(applyCategories(differentProducts, ['Электроника', 'Одежда', 'Для дома'])).toStrictEqual(differentProducts);
    });

    it('empty input categories', () => {
        expect(applyCategories(differentProducts, [])).toStrictEqual(differentProducts);
    });
});

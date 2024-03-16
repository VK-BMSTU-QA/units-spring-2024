import { Product, Category } from "../../types";
import { applyCategories } from "../applyCategories";

const product: Product[] = [
    {
        id: 1,
        name: '1',
        description: '1',
        price: 1,
        priceSymbol: '$',
        category: 'Электроника'
    },
]

const products: Product[] = [
    {
        id: 1,
        name: '1',
        description: '1',
        price: 1,
        priceSymbol: '$',
        category: 'Электроника'
    },
    {
        id: 2,
        name: '1',
        description: '2',
        price: 2,
        priceSymbol: '₽',
        category: 'Для дома',
    },
    {
        id: 3,
        name: '3',
        description: '3',
        price: 3,
        category:  'Одежда',
        imgUrl: '/3.png',
    }
]

describe('test applyCategories', () => {
    it('should return same products on empty categories', () => {
        expect(applyCategories(product, [])).toStrictEqual(product);
    });
    it('should apply all categories', () => {
        expect(applyCategories(products, ['Одежда', 'Электроника', 'Для дома'])).toStrictEqual(products);
    });

    it('should apply one category', () => {
        expect(applyCategories(products, ['Электроника'])).toStrictEqual( [products[0]] );
        expect(applyCategories(products, ['Для дома'])).toStrictEqual( [products[1]] );
        expect(applyCategories(products, ['Одежда'])).toStrictEqual( [products[2]] );
    });

    it('should apply two categories', () => {
        const result = applyCategories(products, ['Одежда', 'Электроника']);
        expect(result).toContainEqual(products[0]);
        expect(result).toContainEqual(products[2]);
        expect(result.length).toBe(2);
    });
});

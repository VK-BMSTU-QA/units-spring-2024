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
        expect(applyCategories(product, [])).toContain(product[0]);
    });
    it('should apply categories', () => {
        expect(applyCategories(products, ['Электроника'])).toContain(product[0]);
        expect(applyCategories(products, ['Для дома'])).toContain(product[1]);
        expect(applyCategories(products, ['Одежда'])).toContain(product[2]);
        expect(applyCategories(products, ['Одежда', 'Электроника', 'Для дома']).length).toBe(3);
    });
});
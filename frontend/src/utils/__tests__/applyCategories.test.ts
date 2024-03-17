import { applyCategories } from '../applyCategories';
import type { Category, PriceSymbol, Product } from '../../types';


const RPODUCTS: Product[] = [
    {
        id: 1,
        name: 'pelmeni',
        description: 'floppa',
        price: 420,
        priceSymbol: '₽' as PriceSymbol,
        category: 'Электроника' as Category,
    },
    {
        id: 2,
        name: 'vareniki',
        description: 'not floppa',
        price: 360,
        priceSymbol: '₽' as PriceSymbol,
        category: 'Для дома' as Category,
    },
    {
        id: 3,
        name: 'сырники',
        description: 'из сыра',
        price: 17,
        priceSymbol: '$' as PriceSymbol,
        category: 'Одежда' as Category,
        imgUrl: '/sirniki.png',
    },
]

describe('test apply categories function', () => {
    it('should return all products if no category passed', () => {
        
        const result = applyCategories(RPODUCTS, []);
        expect(result).toHaveLength(3);
        expect(result).toContain(RPODUCTS[0]);
        expect(result).toContain(RPODUCTS[1]);
        expect(result).toContain(RPODUCTS[2]);
    });
    it('should return filtered by category', () => {
        const result = applyCategories(RPODUCTS, ['Электроника' as Category]);
        expect(result).toHaveLength(1);
        expect(result).toContain(RPODUCTS[0]);
    });
    it('should return array of all products if all categories presents', () => {
        const result = applyCategories(RPODUCTS, ['Электроника' as Category, 'Для дома' as Category, 'Одежда' as Category]);
        expect(result).toHaveLength(3);
        expect(result).toContain(RPODUCTS[0]);
        expect(result).toContain(RPODUCTS[1]);
        expect(result).toContain(RPODUCTS[2]);
    });
});

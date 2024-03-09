import { applyCategories } from '../applyCategories';
import type { Category, PriceSymbol, Product } from '../../types';

describe('test apply categories function', () => {
    it('should return all products if no category passed', () => {
        const prod1 = {
            id: 1,
            name: 'pelmeni',
            description: 'floppa',
            price: 420,
            priceSymbol: '₽' as PriceSymbol,
            category: 'Электроника' as Category,
        };
        const prod2 = {
            id: 2,
            name: 'vareniki',
            description: 'not floppa',
            price: 360,
            priceSymbol: '₽' as PriceSymbol,
            category: 'Для дома' as Category,
        };
        const prod3 = {
            id: 3,
            name: 'сырники',
            description: 'из сыра',
            price: 17,
            priceSymbol: '$' as PriceSymbol,
            category: 'Одежда' as Category,
            imgUrl: '/sirniki.png',
        };
        const result = applyCategories([prod1, prod2, prod3], []);
        expect(result).toHaveLength(3);
        expect(result).toContain(prod1);
        expect(result).toContain(prod2);
        expect(result).toContain(prod3);
    });
    it('should return filtered by category', () => {
        const prod1 = {
            id: 1,
            name: 'pelmeni',
            description: 'floppa',
            price: 420,
            priceSymbol: '₽' as PriceSymbol,
            category: 'Электроника' as Category,
        };
        const prod2 = {
            id: 2,
            name: 'vareniki',
            description: 'not floppa',
            price: 360,
            priceSymbol: '₽' as PriceSymbol,
            category: 'Для дома' as Category,
        };
        const prod3 = {
            id: 3,
            name: 'сырники',
            description: 'из сыра',
            price: 17,
            priceSymbol: '$' as PriceSymbol,
            category: 'Одежда' as Category,
            imgUrl: '/sirniki.png',
        };
        const result = applyCategories([prod1, prod2, prod3], ['Электроника' as Category]);
        expect(result).toHaveLength(1);
        expect(result).toContain(prod1);
    });
    it('should return array of all products if all categories presents', () => {
        const prod1 = {
            id: 1,
            name: 'pelmeni',
            description: 'floppa',
            price: 420,
            priceSymbol: '₽' as PriceSymbol,
            category: 'Электроника' as Category,
        };
        const prod2 = {
            id: 2,
            name: 'vareniki',
            description: 'not floppa',
            price: 360,
            priceSymbol: '₽' as PriceSymbol,
            category: 'Для дома' as Category,
            
        };
        const prod3 = {
            id: 3,
            name: 'сырники',
            description: 'из сыра',
            price: 17,
            priceSymbol: '$' as PriceSymbol,
            category: 'Одежда' as Category,
            imgUrl: '/sirniki.png',
        };
        const result = applyCategories([prod1, prod2, prod3], ['Электроника' as Category, 'Для дома' as Category, 'Одежда' as Category]);
        expect(result).toHaveLength(3);
        expect(result).toContain(prod1);
        expect(result).toContain(prod2);
        expect(result).toContain(prod3);
    });
});

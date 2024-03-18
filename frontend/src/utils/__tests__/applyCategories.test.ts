import { applyCategories } from '../applyCategories';
import { Product, Category, PriceSymbol } from '../../types'

describe('test apply Categories function', () => {
    const prod1: Product = {
        id: 1,
        name: 'пельмени',
        description: 'вкусняшка',
        price: 300,
        priceSymbol: '$',
        category: 'Электроника',
    };
    const prod2: Product = {
        id: 2,
        name: 'пельмени',
        description: 'вкусняшка',
        price: 300,
        priceSymbol: '$',
        category: 'Для дома',
    };
    const prod3: Product = {
        id: 3,
        name: 'пельмени',
        description: 'вкусняшка',
        price: 300,
        priceSymbol: '$',
        category: 'Одежда',
    };
    it('should return array of Products by array of Categories', () => {
        expect(applyCategories([prod1], ['Электроника' as Category])).toStrictEqual([prod1]);
    });

    it('should return array of Products by array of Categories', () => {
        expect(applyCategories([prod1, prod2, prod3], ['Электроника' as Category])).toStrictEqual([prod1]);
    });

    it('should return array of Products by array of Categories', () => {
        expect(applyCategories([prod1, prod2, prod3], ['Для дома' as Category])).toStrictEqual([prod2]);
       
    });

    it('should return array of Products by array of Categories', () => {
        expect(applyCategories([prod1, prod2, prod3], ['Одежда' as Category])).toStrictEqual([prod3]);
       
    });

    it('should return array of Products by array of Categories', () => {
        expect(applyCategories([], ['Одежда' as Category])).toStrictEqual([]);
    });

    it('should return array of Products by array of Categories', () => {
        expect(applyCategories([prod1, prod2], ['Одежда' as Category])).toStrictEqual([]);
    });

    it('should return array of Products by array of Categories', () => {
        expect(applyCategories([prod1, prod2, prod3, prod3], ['Одежда' as Category])).toStrictEqual([prod3, prod3]);
    });

    it('should return array of Products by array of Categories', () => {
        expect(applyCategories([prod1, prod2, prod3, prod3], [])).toStrictEqual([prod1, prod2, prod3, prod3]);
    });
});


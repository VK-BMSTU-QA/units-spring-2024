import type { Product, Category } from '../../types';
import { updateCategories } from '../updateCategories';


describe('test update Categories function', () => {
    it('should return products with current category if product dont contain it, othwewise they must append it', () => {
        
        const categorise: Category[] = ['Для дома', 'Одежда'];
        const category: Category = 'Электроника';

        const new_categorise = updateCategories(categorise, category);
        expect(new_categorise).toEqual(['Для дома', 'Одежда', 'Электроника']);
        expect(updateCategories(new_categorise, category)).toEqual(['Для дома', 'Одежда']);

    });
});
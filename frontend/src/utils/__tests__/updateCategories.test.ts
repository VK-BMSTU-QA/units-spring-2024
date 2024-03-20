import { Categories } from '../../components';
import type { Category, Product } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return update categories', () => {
        const categories1: Category[] = [
            'Для дома',
            'Одежда',
        ]
        const categories2: Category[] = [
            'Одежда',
        ]
        const categories3: Category[] = [
            'Для дома',
            'Одежда',
            'Электроника',
        ]
        const category1: Category = 'Для дома'
        const category2: Category = 'Электроника'
        expect(updateCategories(categories1, category1)).toEqual(categories2);
        expect(updateCategories(categories1, category2)).toEqual(categories3);
    });
});
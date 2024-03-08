import type { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test updateCategories', () => {
    const allCategories: Category[] = ['Одежда', 'Для дома', 'Электроника'];

    it('should add category', () => {
        expect(updateCategories(['Одежда', 'Для дома'], 'Электроника')).toEqual(
            allCategories
        );
    });

    it('should delete category', () => {
        expect(updateCategories(allCategories, 'Одежда')).toEqual([
            'Для дома',
            'Электроника',
        ]);
    });
});

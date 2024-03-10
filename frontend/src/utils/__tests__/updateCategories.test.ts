import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('updateCategories function tests', () => {
    it('should remove the changed category if it exists in current categories', () => {
        const currentCategories: Category[] = ['Электроника', 'Одежда'];
        const changedCategory: Category = 'Электроника';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toEqual(['Одежда']);
    });

    it('should add the changed category if it does not exist in current categories', () => {
        const currentCategories: Category[] = ['Электроника', 'Одежда'];
        const changedCategory: Category = 'Для дома';
        const result = updateCategories(currentCategories, changedCategory);
        expect(result).toEqual(['Электроника', 'Одежда', 'Для дома']);
    });
});

import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('updateCategories function', () => {
    const initialCategories: Category[] = ['Для дома', 'Одежда'];

    it('should add a category if it does not exist in the current list', () => {
        const changedCategory: Category = 'Электроника';
        const result = updateCategories(initialCategories, changedCategory);

        expect(result).toEqual([...initialCategories, changedCategory]);
    });

    it('should remove a category if it exists in the current list', () => {
        const changedCategory: Category = 'Одежда';
        const result = updateCategories(initialCategories, changedCategory);

        expect(result).toEqual(['Для дома']);
    });

    it('should handle adding a category to an empty list', () => {
        const changedCategory: Category = 'Электроника';
        const result = updateCategories([], changedCategory);

        expect(result).toEqual([changedCategory]);
    });

    it('should handle an empty currentCategories list', () => {
        const changedCategory: Category = 'Электроника';
        const result = updateCategories([], changedCategory);

        expect(result).toEqual([changedCategory]);
    });
});

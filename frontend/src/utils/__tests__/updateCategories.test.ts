import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

const INITIAL_CATEGORIES: Category[] = ['Электроника', 'Для дома'];

describe('updateCategories', () => {
    test('should add a new category if not already present', () => {
        const newCategory = 'Одежда';
        const updatedCategories = updateCategories(
            INITIAL_CATEGORIES,
            newCategory
        );
        expect(updatedCategories).toEqual([
            'Электроника',
            'Для дома',
            'Одежда',
        ]);
    });

    test('should remove a category if already present', () => {
        const existingCategory = 'Для дома';
        const updatedCategories = updateCategories(
            INITIAL_CATEGORIES,
            existingCategory
        );
        expect(updatedCategories).toEqual(['Электроника']);
    });
});

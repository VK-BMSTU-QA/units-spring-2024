import { updateCategories } from '../updateCategories';
import { Category } from '../../types';

describe('test update categories function', () => {
    it.each([
        [['Одежда'], 'Одежда', []],
        [['Одежда', 'Электроника'], 'Одежда', ['Электроника']],
        [['Одежда', 'Электроника', 'Для дома'], 'Одежда', ['Электроника', 'Для дома']],
        [['Одежда', 'Электроника', 'Для дома'], 'Электроника', ['Одежда', 'Для дома']],
        [[], 'Одежда', ['Одежда']],
    ] as [Category[], Category, Category[]][])('should return correct categories', (currentCategories: Category[], changedCategories: Category, expected: Category[]) => {
        expect(updateCategories(currentCategories, changedCategories)).toStrictEqual(expected);   
    });

    it('should remove a category if it is in the list', () => {

        const changedCategory: Category = 'Электроника';
        const result = updateCategories(['Электроника', 'Одежда'], changedCategory);

        expect(result).toEqual(['Одежда']);
    });

    it('should handle adding a category to an empty list', () => {
        const changedCategory: Category = 'Одежда';
        const result = updateCategories([], changedCategory);

        expect(result).toEqual([changedCategory]);
    });
});

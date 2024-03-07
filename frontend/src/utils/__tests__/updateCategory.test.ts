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
});

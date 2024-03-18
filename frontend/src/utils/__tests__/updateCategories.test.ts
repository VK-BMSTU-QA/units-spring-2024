import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

const currCategories: Category[] = [
    'Электроника', 'Для дома'
]

describe('test update categories function', () => {
    it('should add the new category to the categories list', () => {
        expect(updateCategories(
            currCategories, 
            'Одежда')
        ).toStrictEqual(
            [...currCategories, 'Одежда'],
        );
    });
    it('should remove the category if it already exists', () => {
        expect(updateCategories(
            currCategories,
            'Для дома')
        ).toStrictEqual(
            [currCategories[0]]
        );
        expect(updateCategories(
            currCategories,
            'Электроника')
        ).toStrictEqual(
            [currCategories[1]]
        );
    });
});

import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('test update categories function', () => {
    const categories: Category[] = ['Электроника', 'Для дома', 'Одежда'];

    const electronic: Category = 'Электроника';
    const home: Category = 'Для дома';
    const clothes: Category = 'Одежда';

    const outElectronic: Category[] = ['Для дома', 'Одежда'];
    const outHome: Category[] = ['Электроника', 'Одежда'];
    const outClothes: Category[] = ['Электроника', 'Для дома'];

    test.each([
        [categories, electronic, outElectronic],
        [categories, home, outHome],
        [categories, clothes, outClothes],
    ])('categories has category', (categories, category, expected) => {
        expect(updateCategories(categories, category)).toStrictEqual(expected);
    });

    test.each([
        [outElectronic, electronic, [...outElectronic, electronic]],
        [outHome, home, [...outHome, home]],
        [outClothes, clothes, [...outClothes, clothes]],
    ])('categories has not category', (categories, category, expected) => {
        expect(updateCategories(categories, category)).toStrictEqual(expected);
    });
});

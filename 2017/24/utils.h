#ifndef UTILS_H_INCLUDED
#define UTILS_H_INCLUDED

template <typename Collection,typename Predicate>
Collection filterNot(Collection col,Predicate predicate ) {
    auto returnIterator = std::remove_if(col.begin(),col.end(),predicate);
    col.erase(returnIterator,std::end(col));
    return col;
}

template <typename Collection,typename Predicate>
Collection filter(Collection col,Predicate predicate) {
    //capture the predicate in order to be used inside function
    auto fnCol = filterNot(col,[predicate](typename Collection::value_type i) {
        return !predicate(i);
    });
    return fnCol;
}

#endif // UTILS_H_INCLUDED

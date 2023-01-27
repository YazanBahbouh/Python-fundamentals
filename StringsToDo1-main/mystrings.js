
String.prototype.removeBlanks = function() {
    let sArray = this.split("")

    let b = sArray.filter( (a)=> (a != ' '))
    let c = b.join('')

    return c
}
let a = " Pl ayTha tF u nkyM usi c "
console.log(a.removeBlanks())


String.prototype.getDigits = function() {
    let sArray = this.split("")

    let b = sArray.filter( (e) => !isNaN(e))
    let c = Number(b.join(''))
    return c
}
console.log("abc8c0d1ngd0j0!8".getDigits())


String.prototype.acronym = function(){
    let words = this.toUpperCase().split(" ")
    let b = words.map( a => (a.charAt(0))).join("")

    return b
}
console.log("Hi my name is - poo".acronym())


String.prototype.countNonSpaces = function() {
    let numSpaces = 0
    for(let i = 0; i< this.length; i++){
        if (this.charAt(i) === ' '){
            numSpaces++
        }
    }
    return this.length - numSpaces
}
console.log("Hi there".countNonSpaces())


Array.prototype.removeShorterStrings = function() {
    let a = this.filter( (e) => (e.length > 4) )

    return a
}
console.log(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'].removeShorterStrings())


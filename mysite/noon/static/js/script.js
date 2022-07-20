const swiper = new Swiper('.swiper', {
  direction: 'horizontal',

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  breakpoints: {
    600: {
        slidesPerView: 2,
        slidesPerGroup: 2,
        spaceBetween: 20,
            },
    900: {
        slidesPerView: 3,
        slidesPerGroup: 3,
        spaceBetween: 20,
        allowSlidePrev: true,
        allowSlideNext: true
            },
    1200: {
        slidesPerView: 5,
        slidesPerGroup: 5,
        spaceBetween: 20,
        allowSlidePrev: true,
        allowSlideNext: true
            }
  }
  
});

console.log('labas')
//demonstration

//const swiperSlides = document.getElementsByClassName('swiper-slide')
//const images = ["https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80", "https://images.unsplash.com/photo-1454496522488-7a8e488e8606?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80", "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80", "https://images.unsplash.com/photo-1519681393784-d120267933ba?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80", "https://images.unsplash.com/photo-1458668383970-8ddd3927deed?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1167&q=80"]
//for(var x of swiperSlides){
//    x.addEventListener('click', function(){
//        let index = swiper.clickedIndex
//
//        let img = document.createElement("img")
//        img.classList.add("demonstration")
//        img.setAttribute("src", images[index])
//        document.body.append(img)
//        //add event listener
//        img.addEventListener("click", function(){
//            this.remove()
//        })
//    })
//}
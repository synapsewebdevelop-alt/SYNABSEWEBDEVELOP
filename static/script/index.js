let a=document.getElementById('scrollToTopBtn');
window.onscroll=function(){
    scrollfunction();
}
function scrollfunction(){
    if(document.body.scrollTop > 100 || document.documentElement.scrollTop >100){
        a.style.display= "block";
    }else{
        a.style.display="none";
    }
}


document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        const navbar = document.querySelector('.navbar-collapse');
        if (navbar.classList.contains('show')) {
          const bsCollapse = new bootstrap.Collapse(navbar, { toggle: true });
          bsCollapse.hide();
        }
      });
    });

document.getElementById('submitBtn').addEventListener('click',function(event){
  
  setTimeout(() =>{
    this.reset();
  },1000);
});

Vue.config.devtools = true;

var app = new Vue({
  el: '#app',
  delimiters:["${","}"],
  data: {
    projects: [],
    showMedia: false,
    media: [],
    currentID: null,
  },
  mounted(){
    axios.get('http://localhost:8000/gallery/api/projects').then((res) => {
      if(res.data.status == 200){
        this.projects = res.data.data;
      }
    }).catch( err => { 
      console.log(err); 
    });
  },
  methods: {
    getMedia: function(pk){
      axios.get('http://localhost:8000/gallery/api/media/' + pk).then(res =>{
        if(res.data.status == 200){
          if(res.data.data){
            this.media = res.data.data;
            this.showMedia = true;
          }
        }
      }).catch(err => { 
        console.log(err); 
      });
    },
    closeOverlay: function(){
      this.showMedia = false;
    },
    hoverTitle: function(e){
      console.dir(e.target.querySelector('.projectTitle'));
      var seq = e.target.getAttribute('seq')
    },
  },
});
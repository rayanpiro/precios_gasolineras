Vue.createApp({
  data() {
    return {
      stations: [{
        result: {
          name: 'A',
        },
      }],
      url_to_save: null,
    }
  },

  mounted() {
    let uri = window.location.search.substring(1)
    let params = new URLSearchParams(uri)

    for( const [key,value] of params.entries()) {
      this.$refs[key].value = value
    }
    
    this.get_stations()    
  },

  methods: {
    async get_stations() {

      const ccaa = this.$refs.ccaa.value
      const petrol = this.$refs.petrol.value
      const distance = this.$refs.distance.value
      const lat = this.$refs.lat.value
      const lon = this.$refs.lon.value
      const num_results = this.$refs.num_results.value

      query = '?'

      if (ccaa != "Todas") {
        query+='ccaa='+ccaa+'&'
      }

      if (petrol != "Todas") {
        query+='petrol='+petrol+'&'
      }

      if (distance != "") {
        query+='distance='+distance+'&'
      }

      if (lat != "") {
        query+='lat='+lat+'&'
      }
      
      if (lon != "") {
        query+='lon='+lon+'&'
      }

      if (query==='?') {
        query = ''
      }

      const url = num_results+query
      
      const res = await fetch(url)
      this.stations = await res.json()

      this.$refs.results.classList.remove("d-none")
      
      this.url_to_save = query
      if(query != '') {
        this.$refs.save_url.classList.remove("d-none")
      }
      return res
    }
    
  },
  delimiters: ['{','}'],
}).mount('#app')
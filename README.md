# LP-Projekts
## projekta apraksts
Projekta uzdevums ir atvieglot studentiem laika plānošanu, vieglākā formātā parādot termiņus darbiem. Programmatūra automātiski iegūst datus no e-studijām un attēlo tos lietotāja saskarsmē, kurā dod iespēju aizsūtīt attgādinājumu uz lietātāja ievadītu e-pastu.
## izmantotās Python bibliotēkas
### Selenium
nepieciešams lai tiktu pie un iegūtu datus no e-studiju vides.
### time
nepieciešams lai ievadītu nepieciešamas pauzes kodā.
### PySimpleGUI
nepieciešams lai tiktu izveidota lietotāj saskarsme.
### schedule
nepieciešams lai tiktu izsūtīts atgādinājums nepieciešamajā laikā.
### datetime
nepieciešams lai notiektu, kad ir jaizsūta atgādinājums.
### smtplib, email.mime.text un email.mime.multipart
nepieciešams lai varētu izsūtīt atgādinājumu.
## izmatošanas metodes
Lietotājs ievada savus ortus datus, lai tiktu pie e-studijām. Tālāk lietotājam ir jāievada e-pasts uz kuru tiks nosūtīts atgādinājums par darba termiņa beigām, ja to izvēlēsies. Pēc datu ievades tiek igūti dati (darba nosaukums, kurss un termiņš) no e-stujas vides un tie tiek attēloti lietotāj saskarsmē. Lietotājs pēc izvēles var pieprasīt atgādinājumu, kurš tiks atsūtīts dienu pirms darba nodošanas 12.00.

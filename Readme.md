# Conciliador de Pasarelas de Pago
## Qué detecta, por qué importa y cómo actuar

---

## El problema que resuelve

Cuando una empresa recibe pagos con tarjeta de crédito, intervienen tres sistemas distintos que deben coincidir al final del mes:

- **El ERP o sistema contable** registra cada venta en el momento en que ocurre. Muestra el valor bruto de la factura — lo que el cliente pagó.
- **La pasarela de pago** (Datafast, Medianet, PayPhone) procesa la transacción y cobra su comisión por el servicio.
- **El banco** recibe los fondos de la pasarela, aplica las retenciones que exige el SRI y deposita el valor neto en la cuenta del comercio.

El problema es que estos tres sistemas no se comunican entre sí de forma automática. El equipo contable tiene que cruzar manualmente los reportes de los tres — un proceso que con volúmenes medianos puede tomar entre 8 y 20 horas semanales y que, inevitablemente, genera errores humanos.

---

## Cómo fluye el dinero — la base para entender las novedades

Antes de explicar los errores que el sistema detecta, es importante entender cómo fluye el dinero en cada transacción con tarjeta.

Cuando un cliente paga $500 con su tarjeta Visa, esto es lo que ocurre:

**1. El cliente paga $500**
Su banco — el banco que emitió su tarjeta, llamado banco emisor — autoriza el cobro y reserva los fondos.

**2. La pasarela procesa la transacción y cobra su comisión**
Datafast, por ejemplo, cobra el 3.5% sobre el valor bruto. De los $500 descuenta $17.50 y envía $482.50 al banco del comercio.

**3. El banco del comercio aplica las retenciones del SRI**
El banco adquirente — el banco donde el comercio tiene su cuenta — actúa como agente de retención. Por obligación legal descuenta la retención de IVA (4.5% sobre el valor bruto = $22.50) y la retención en la fuente de renta (1% = $5.00).

**4. El banco deposita el valor neto**
Después de todos los descuentos, el comercio recibe $455.00 — no los $500.00 que pagó el cliente.

```
Cliente paga              $500.00
Comisión Datafast (3.5%)  - $17.50
Retención IVA (4.5%)      - $22.50
Retención renta (1%)      - $  5.00
                          ─────────
Depósito recibido         $455.00
```

Este desfase entre lo que registra el ERP ($500) y lo que deposita el banco ($455) es completamente normal y esperado. El conciliador conoce estas reglas y las aplica automáticamente para cada transacción — eso le permite distinguir entre una diferencia esperada y un error real.

---

## Las tres novedades que el script detecta

De un total de 3.000 transacciones analizadas en el período julio-diciembre 2024, el sistema identificó 99 casos que requieren atención:

```

![Resultado Conciliador](Consola%20reconciliador.JPG)

Transacciones conciliadas correctamente  →  2.901  (96.7%)
Comisiones cobradas de más               →     45  casos
Chargebacks no registrados en ERP        →     24  casos
Transacciones sin confirmar en pasarela  →     30  casos
```

---

### Novedad 1 — Comisiones cobradas de más por la pasarela

**Qué significa**

La pasarela cobró un porcentaje de comisión mayor al acordado en el contrato. Por ejemplo, el contrato con Datafast establece una tasa del 3.5%, pero en 45 transacciones cobró entre 4.0% y 5.0%.

**Por qué ocurre**

Las pasarelas aplican tarifas distintas según el tipo de tarjeta, el país de emisión o la categoría del comercio. Cuando el sistema clasifica incorrectamente una transacción, aplica una tarifa más alta. Sin un sistema de verificación, ese sobrecargo pasa desapercibido.

**El impacto económico**

En el período analizado las pasarelas cobraron $100.70 más de lo estipulado en los contratos. Este monto es completamente recuperable mediante un reclamo formal.

**Cómo lo resuelve el contador**

El reporte muestra por cada transacción el monto de la factura, la comisión que debía cobrarse según contrato, la comisión que se cobró realmente y la diferencia a reclamar.

Con esa información el contador:

1. Agrupa las diferencias por pasarela para obtener el total a reclamar a cada una.
2. Genera una carta de reclamo formal con el detalle de cada transacción afectada, la referencia del contrato y el monto total a devolver.
3. Una vez que la pasarela procesa la devolución, registra el ajuste contable correspondiente.

---

### Novedad 2 — Chargebacks no registrados en el ERP

**Qué es un chargeback**

Un chargeback ocurre cuando un cliente disputa un cobro con su banco. El cliente llama a su banco — el banco emisor — y dice "no reconozco este cargo" o "el producto nunca llegó". El banco emisor investiga y, si considera válida la disputa, devuelve el dinero al cliente y se lo descuenta al comercio.

Este proceso es completamente automático y unilateral — el banco no pide autorización al comercio. Simplemente revierte el depósito y lo notifica después mediante el reporte de liquidación, donde la transacción aparece con un monto negativo.

**El problema**

El banco revirtió 24 transacciones por un total de $5,060.69. Esas reversiones aparecen en el reporte bancario como montos negativos. Sin embargo, el ERP nunca fue actualizado — las facturas correspondientes siguen marcadas como pagadas.

Esto significa que el sistema contable muestra $5,060.69 en ingresos que en realidad ya no existen en la cuenta bancaria.

**El impacto contable**

Si este error no se corrige antes del cierre contable, el estado de resultados está inflado en $5,060.69. La empresa cree que cobró ese dinero cuando en realidad ya fue devuelto al cliente.

**Cómo lo resuelve el contador**

El reporte muestra cada chargeback con su fecha, pasarela y monto revertido.

Con esa información el contador:

1. Localiza cada factura en el ERP usando el código de transacción.
2. Registra una nota de crédito o asiento de reversión para anular el ingreso contabilizado.
3. Verifica si el chargeback puede ser disputado — el comercio tiene un plazo definido para presentar evidencia ante la pasarela y recuperar el dinero si el cobro era legítimo.
4. Si el plazo venció o la disputa no procede, registra la pérdida definitiva.

---

### Novedad 3 — Transacciones sin confirmar en la pasarela

**Qué significa**

Son 30 transacciones que el banco liquidó y el ERP registró correctamente — los montos cuadran — pero que no aparecen en el reporte de la pasarela.

A diferencia de los dos casos anteriores, aquí no hay una diferencia de dinero. El problema es de trazabilidad: no hay evidencia de que la pasarela participó en el procesamiento de esas transacciones.

**Por qué importa**

Sin la confirmación de la pasarela no es posible verificar qué comisión cobró ni auditar si el procesamiento fue correcto. En una revisión externa o auditoría tributaria, esa falta de trazabilidad genera observaciones de control interno.

Además, en casos extremos puede indicar que el pago llegó por un canal no autorizado o que hubo un error en el procesamiento que requiere investigación.

**Cómo lo resuelve el contador**

El reporte muestra cada transacción con su fecha, pasarela asignada y los montos registrados en banco y ERP.

Con esa información el contador:

1. Contacta a la pasarela con el listado de transacciones sin confirmar y solicita una explicación.
2. Si la pasarela confirma que las procesó y fue un error de reporte, solicita el reporte corregido y verifica que las comisiones sean correctas.
3. Si la pasarela no tiene registro de esas transacciones, investiga el canal real del pago — puede ser una transferencia directa, un depósito en efectivo u otro medio — y actualiza el registro en el ERP con el canal correcto.

---

## El valor que aporta el proyecto

Antes de este sistema, un equipo contable dedicaba entre 8 y 20 horas semanales a cruzar manualmente los reportes del banco, la pasarela y el ERP. Aun así, errores como las comisiones cobradas de más o los chargebacks no registrados pasaban desapercibidos porque el volumen de transacciones hace imposible revisar cada línea con atención.

Con el sistema ese trabajo toma menos de un minuto. El pipeline automatizado lee los tres reportes, aplica las reglas del SRI y los contratos de cada pasarela, cruza las transacciones y clasifica cada una con su estado y tipo de novedad. El resultado es un dashboard ejecutivo que el gerente financiero puede leer en 30 segundos y un detalle operativo que el contador puede usar para actuar de inmediato.

El impacto más concreto en el período analizado: $100.70 en comisiones recuperables que sin el sistema nadie hubiera reclamado, y $5,060.69 en ingresos ficticios que hubieran cerrado el período en los libros contables sin ser detectados.

